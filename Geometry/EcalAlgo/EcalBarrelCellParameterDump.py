import FWCore.ParameterSet.Config as cms

def EcalBarrelCellParameterDump(**kwargs):
  mod = cms.EDAnalyzer('EcalBarrelCellParameterDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
