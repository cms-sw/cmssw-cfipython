import FWCore.ParameterSet.Config as cms

def CSCDigiDump(**kwargs):
  mod = cms.EDAnalyzer('CSCDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
