import FWCore.ParameterSet.Config as cms

def EtMinCaloJetCountFilter(*args, **kwargs):
  mod = cms.EDFilter('EtMinCaloJetCountFilter',
    src = cms.InputTag(''),
    etMin = cms.double(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
