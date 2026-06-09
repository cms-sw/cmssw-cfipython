import FWCore.ParameterSet.Config as cms

from .DeepDoubleXONNXJetTagsProducer import DeepDoubleXONNXJetTagsProducer

pfDeepDoubleCvBJetTags = DeepDoubleXONNXJetTagsProducer(

  flav_names = cms.vstring(
    'probHbb',
    'probHcc'
  ),
  flavor = 'CvB',
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB.onnx')
)
