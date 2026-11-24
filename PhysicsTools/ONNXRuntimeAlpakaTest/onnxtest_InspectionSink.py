import FWCore.ParameterSet.Config as cms

def onnxtest_InspectionSink(*args, **kwargs):
  mod = cms.EDAnalyzer('onnxtest::InspectionSink',
    particles = cms.required.InputTag,
    simple_net = cms.required.InputTag,
    simple_net_feature_major = cms.required.InputTag,
    simple_net_minibatch = cms.required.InputTag,
    masked_net = cms.required.InputTag,
    masked_net_reversed = cms.required.InputTag,
    masked_net_empty_mask = cms.required.InputTag,
    multi_head_net = cms.required.InputTag,
    resnet = cms.required.InputTag,
    resnet_minibatch = cms.required.InputTag,
    hits = cms.required.InputTag,
    scaled_net = cms.required.InputTag,
    scaled_net_minibatch = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
