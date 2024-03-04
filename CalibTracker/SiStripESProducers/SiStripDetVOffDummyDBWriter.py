import FWCore.ParameterSet.Config as cms

def SiStripDetVOffDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
