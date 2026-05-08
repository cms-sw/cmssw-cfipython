import FWCore.ParameterSet.Config as cms

def torchtest_InspectionSink(*args, **kwargs):
  mod = cms.EDAnalyzer('torchtest::InspectionSink',
    environment = cms.untracked.int32(0),
    particles = cms.required.InputTag,
    simple_net = cms.required.InputTag,
    simple_net_minibatch = cms.required.InputTag,
    masked_net = cms.required.InputTag,
    multi_head_net = cms.required.InputTag,
    images = cms.required.InputTag,
    resnet18 = cms.required.InputTag,
    resnet18_minibatch = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
