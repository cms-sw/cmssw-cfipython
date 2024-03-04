import FWCore.ParameterSet.Config as cms

def FakeCPEFiller(**kwargs):
  mod = cms.EDFilter('FakeCPEFiller',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
