import FWCore.ParameterSet.Config as cms

from .DeepDoubleXONNXJetTagsProducer import DeepDoubleXONNXJetTagsProducer

pfDeepDoubleCvLJetTags = DeepDoubleXONNXJetTagsProducer(
  src = ('pfDeepDoubleXTagInfos'),
  input_names = [
    'input_1',
    'input_2',
    'input_3'
  ],
  output_names = [],
  version = 'V1',
  flavor = 'CvL',
  flav_names = cms.vstring(
    'probQCD',
    'probHcc'
  ),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC.onnx')
)
