import FWCore.ParameterSet.Config as cms

def PFClusterMETProducer(*args, **kwargs):
  mod = cms.EDProducer('PFClusterMETProducer',
    src = cms.InputTag(''),
    globalThreshold = cms.double(0),
    alias = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
