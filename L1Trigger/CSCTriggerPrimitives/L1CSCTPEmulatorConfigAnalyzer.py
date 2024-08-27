import FWCore.ParameterSet.Config as cms

def L1CSCTPEmulatorConfigAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1CSCTPEmulatorConfigAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
