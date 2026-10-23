import FWCore.ParameterSet.Config as cms

def EcalPreshowerCellParameterDump(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPreshowerCellParameterDump',
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
