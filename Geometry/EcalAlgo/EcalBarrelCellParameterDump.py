import FWCore.ParameterSet.Config as cms

def EcalBarrelCellParameterDump(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalBarrelCellParameterDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
