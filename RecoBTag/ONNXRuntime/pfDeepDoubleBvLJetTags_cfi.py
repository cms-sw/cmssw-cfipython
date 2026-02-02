import FWCore.ParameterSet.Config as cms

from .DeepDoubleXONNXJetTagsProducer import DeepDoubleXONNXJetTagsProducer

pfDeepDoubleBvLJetTags = DeepDoubleXONNXJetTagsProducer(
  src = ('pfDeepDoubleXTagInfos'),
  input_names = [
    'input_1',
    'input_2',
    'input_3'
  ],
  output_names = [],
  version = 'V1',
  flavor = 'BvL',
  flav_names = cms.vstring(
    'probQCD',
    'probHbb'
  ),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDB.onnx')
)
