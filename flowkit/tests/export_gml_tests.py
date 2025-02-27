"""
Tests for exporting to GatingML
"""
import unittest
import sys
import os
import glob
import re
from io import BytesIO
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath('../..'))

from flowkit import Sample, Session

data1_fcs_path = 'data/gate_ref/data1.fcs'
data1_sample = Sample(data1_fcs_path)


class ExportGMLTestCase(unittest.TestCase):
    @staticmethod
    def test_min_range_gate():
        gml_path = 'data/gate_ref/gml/gml_range_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Range1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Range1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_rect1_gate():
        gml_path = 'data/gate_ref/gml/gml_rect1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Rectangle1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Rectangle1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_rect2_gate():
        gml_path = 'data/gate_ref/gml/gml_rect2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Rectangle2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Rectangle2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_poly1_gate():
        gml_path = 'data/gate_ref/gml/gml_poly1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Polygon1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Polygon1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_poly2_gate():
        gml_path = 'data/gate_ref/gml/gml_poly2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Polygon2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Polygon2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_poly3_non_solid_gate():
        gml_path = 'data/gate_ref/gml/gml_poly3ns_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Polygon3NS.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Polygon3NS')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_ellipse1_gate():
        gml_path = 'data/gate_ref/gml/gml_ellipse1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Ellipse1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Ellipse1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_ellipsoid_3d_gate():
        gml_path = 'data/gate_ref/gml/gml_ellipsoid3d_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Ellipsoid3D.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Ellipsoid3D')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_time_range_gate():
        gml_path = 'data/gate_ref/gml/gml_time_range_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Range2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Range2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_quadrant1_gate():
        gml_path = 'data/gate_ref/gml/gml_quadrant1_gate.xml'
        res1_path = 'data/gate_ref/truth/Results_FL2N-FL4N.txt'
        res2_path = 'data/gate_ref/truth/Results_FL2N-FL4P.txt'
        res3_path = 'data/gate_ref/truth/Results_FL2P-FL4N.txt'
        res4_path = 'data/gate_ref/truth/Results_FL2P-FL4P.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth1 = pd.read_csv(res1_path, header=None, dtype='bool').squeeze().values
        truth2 = pd.read_csv(res2_path, header=None, dtype='bool').squeeze().values
        truth3 = pd.read_csv(res3_path, header=None, dtype='bool').squeeze().values
        truth4 = pd.read_csv(res4_path, header=None, dtype='bool').squeeze().values

        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth1, result.get_gate_membership('FL2N-FL4N'))
        np.testing.assert_array_equal(truth2, result.get_gate_membership('FL2N-FL4P'))
        np.testing.assert_array_equal(truth3, result.get_gate_membership('FL2P-FL4N'))
        np.testing.assert_array_equal(truth4, result.get_gate_membership('FL2P-FL4P'))

    @staticmethod
    def test_quadrant2_gate():
        gml_path = 'data/gate_ref/gml/gml_quadrant2_gate.xml'
        res1_path = 'data/gate_ref/truth/Results_FSCN-SSCN.txt'
        res2_path = 'data/gate_ref/truth/Results_FSCD-SSCN-FL1N.txt'
        res3_path = 'data/gate_ref/truth/Results_FSCP-SSCN-FL1N.txt'
        res4_path = 'data/gate_ref/truth/Results_FSCD-FL1P.txt'
        res5_path = 'data/gate_ref/truth/Results_FSCN-SSCP-FL1P.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth1 = pd.read_csv(res1_path, header=None, dtype='bool').squeeze().values
        truth2 = pd.read_csv(res2_path, header=None, dtype='bool').squeeze().values
        truth3 = pd.read_csv(res3_path, header=None, dtype='bool').squeeze().values
        truth4 = pd.read_csv(res4_path, header=None, dtype='bool').squeeze().values
        truth5 = pd.read_csv(res5_path, header=None, dtype='bool').squeeze().values

        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth1, result.get_gate_membership('FSCN-SSCN'))
        np.testing.assert_array_equal(truth2, result.get_gate_membership('FSCD-SSCN-FL1N'))
        np.testing.assert_array_equal(truth3, result.get_gate_membership('FSCP-SSCN-FL1N'))
        np.testing.assert_array_equal(truth4, result.get_gate_membership('FSCD-FL1P'))
        np.testing.assert_array_equal(truth5, result.get_gate_membership('FSCN-SSCP-FL1P'))

    @staticmethod
    def test_ratio_range1_gate():
        gml_path = 'data/gate_ref/gml/gml_ratio_range1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_RatRange1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'RatRange1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_ratio_range2_gate():
        gml_path = 'data/gate_ref/gml/gml_ratio_range2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_RatRange2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'RatRange2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_log_ratio_range1_gate():
        gml_path = 'data/gate_ref/gml/gml_log_ratio_range1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_RatRange1a.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'RatRange1a')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_and1_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_and1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_And1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'And1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_and2_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_and2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_And2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'And2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_or1_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_or1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Or1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Or1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_and3_complement_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_and3_complement_gate.xml'
        res_path = 'data/gate_ref/truth/Results_And3.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'And3')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_not1_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_not1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Not1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Not1')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_and4_not_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_and4_not_gate.xml'
        res_path = 'data/gate_ref/truth/Results_And4.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'And4')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_boolean_or2_complement_gate():
        gml_path = 'data/gate_ref/gml/gml_boolean_or2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Or2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Or2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_matrix_poly4_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_poly4_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Polygon4.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Polygon4')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_matrix_rect3_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_rect3_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Rectangle3.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Rectangle3')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_matrix_rect4_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_rect4_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Rectangle4.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Rectangle4')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_matrix_rect5_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_rect5_gate.xml'
        res_path = 'data/gate_ref/truth/Results_Rectangle5.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'Rectangle5')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_transform_asinh_range1_gate():
        gml_path = 'data/gate_ref/gml/gml_transform_asinh_range1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange1'))

    @staticmethod
    def test_transform_hyperlog_range2_gate():
        gml_path = 'data/gate_ref/gml/gml_transform_hyperlog_range2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'ScaleRange2')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_transform_linear_range3_gate():
        gml_path = 'data/gate_ref/gml/gml_transform_linear_range3_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange3.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'ScaleRange3')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_transform_logicle_range4_gate():
        gml_path = 'data/gate_ref/gml/gml_transform_logicle_range4_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange4.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'ScaleRange4')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_transform_logicle_range5_gate():
        gml_path = 'data/gate_ref/gml/gml_transform_logicle_range5_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange5.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'ScaleRange5')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_transform_log_range6_gate():
        gml_path = 'data/gate_ref/gml/gml_transform_log_range6_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange6.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gate_membership(data1_sample.id, 'ScaleRange6')

        np.testing.assert_array_equal(truth, result)

    @staticmethod
    def test_matrix_transform_asinh_range1c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_asinh_range1c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange1c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange1c'))

    @staticmethod
    def test_matrix_transform_hyperlog_range2c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_hyperlog_range2c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange2c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange2c'))

    @staticmethod
    def test_matrix_transform_linear_range3c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_linear_range3c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange3c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange3c'))

    @staticmethod
    def test_matrix_transform_logicle_range4c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_logicle_range4c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange4c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange4c'))

    @staticmethod
    def test_matrix_transform_logicle_range5c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_logicle_range5c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange5c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange5c'))

    @staticmethod
    def test_matrix_transform_asinh_range6c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_asinh_range6c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange6c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange6c'))

    @staticmethod
    def test_matrix_transform_hyperlog_range7c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_hyperlog_range7c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange7c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange7c'))

    @staticmethod
    def test_matrix_transform_logicle_range8c_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_logicle_range8c_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRange8c.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRange8c'))

    @staticmethod
    def test_matrix_transform_logicle_rect1_gate():
        gml_path = 'data/gate_ref/gml/gml_matrix_transform_logicle_rect1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScaleRect1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScaleRect1'))

    @staticmethod
    def test_parent_poly1_boolean_and2_gate():
        gml_path = 'data/gate_ref/gml/gml_parent_poly1_boolean_and2_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ParAnd2.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ParAnd2'))

    @staticmethod
    def test_parent_range1_boolean_and3_gate():
        gml_path = 'data/gate_ref/gml/gml_parent_range1_boolean_and3_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ParAnd3.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ParAnd3'))

    @staticmethod
    def test_parent_rect1_rect_par1_gate():
        gml_path = 'data/gate_ref/gml/gml_parent_rect1_rect_par1_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ScalePar1.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ScalePar1'))

    @staticmethod
    def test_parent_quadrant_rect_gate():
        gml_path = 'data/gate_ref/gml/gml_parent_quadrant_rect_gate.xml'
        res_path = 'data/gate_ref/truth/Results_ParQuadRect.txt'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values
        result = sess_out.get_gating_results(data1_sample.id)

        np.testing.assert_array_equal(truth, result.get_gate_membership('ParRectangle1'))

    @staticmethod
    def test_all_gates():
        gml_path = 'data/gate_ref/gml/gml_all_gates.xml'

        s = Session(gating_strategy=gml_path)

        out_file = BytesIO()
        s.export_gml(out_file)
        out_file.seek(0)

        sess_out = Session(gating_strategy=out_file)
        sess_out.add_samples(data1_sample)
        sess_out.analyze_samples()

        gs_results = sess_out.get_gating_results(data1_sample.id)

        truth_pattern = 'data/gate_ref/truth/Results*.txt'
        res_files = glob.glob(truth_pattern)
        truth_dict = {}

        for res_path in res_files:
            match = re.search("Results_(.+)\\.txt$", res_path)
            if match is not None:
                g_id = match.group(1)
                truth = pd.read_csv(res_path, header=None, dtype='bool').squeeze().values

                truth_dict[g_id] = truth

        for row in gs_results.report.itertuples():
            np.testing.assert_array_equal(
                truth_dict[row.gate_name],
                gs_results.get_gate_membership(row.gate_name)
            )
