import FWCore.ParameterSet.Config as cms

def MuonCountFilter(**kwargs):
  mod = cms.EDFilter('MuonCountFilter',
    src = cms.InputTag(''),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
