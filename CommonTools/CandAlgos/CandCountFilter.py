import FWCore.ParameterSet.Config as cms

def CandCountFilter(**kwargs):
  mod = cms.EDFilter('CandCountFilter',
    src = cms.InputTag(''),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod