import FWCore.ParameterSet.Config as cms

from .DeepDoubleXONNXJetTagsProducer import DeepDoubleXONNXJetTagsProducer

pfDeepDoubleCvLJetTags = DeepDoubleXONNXJetTagsProducer(

  flav_names = cms.vstring(
    'probQCD',
    'probHcc'
  ),
  flavor = 'CvL',
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC.onnx')
)
