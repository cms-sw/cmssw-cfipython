import FWCore.ParameterSet.Config as cms

def EtMinSuperClusterCountFilter(*args, **kwargs):
  mod = cms.EDFilter('EtMinSuperClusterCountFilter',
    src = cms.InputTag(''),
    etMin = cms.double(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
