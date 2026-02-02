import FWCore.ParameterSet.Config as cms

from .DeepDoubleXONNXJetTagsProducer import DeepDoubleXONNXJetTagsProducer

pfDeepDoubleCvBJetTags = DeepDoubleXONNXJetTagsProducer(
  src = ('pfDeepDoubleXTagInfos'),
  input_names = [
    'input_1',
    'input_2',
    'input_3'
  ],
  output_names = [],
  version = 'V1',
  flavor = 'CvB',
  flav_names = cms.vstring(
    'probHbb',
    'probHcc'
  ),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB.onnx')
)
