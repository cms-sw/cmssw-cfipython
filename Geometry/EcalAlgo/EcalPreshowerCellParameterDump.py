import FWCore.ParameterSet.Config as cms

def EcalPreshowerCellParameterDump(**kwargs):
  mod = cms.EDAnalyzer('EcalPreshowerCellParameterDump',
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
