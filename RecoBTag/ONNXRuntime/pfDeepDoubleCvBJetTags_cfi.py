import FWCore.ParameterSet.Config as cms

pfDeepDoubleCvBJetTags = cms.EDProducer('DeepDoubleXONNXJetTagsProducer',
  src = cms.InputTag('pfDeepDoubleXTagInfos'),
  input_names = cms.vstring(
    'input_1',
    'input_2',
    'input_3'
  ),
  output_names = cms.vstring(),
  version = cms.string('V1'),
  flavor = cms.string('CvB'),
  flav_names = cms.vstring(
    'probHbb',
    'probHcc'
  ),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB.onnx')
)
