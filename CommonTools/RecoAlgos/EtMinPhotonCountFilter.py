import FWCore.ParameterSet.Config as cms

def EtMinPhotonCountFilter(**kwargs):
  mod = cms.EDFilter('EtMinPhotonCountFilter',
    src = cms.InputTag(''),
    etMin = cms.double(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
