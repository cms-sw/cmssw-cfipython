import FWCore.ParameterSet.Config as cms

def ProduceAgingObject(**kwargs):
  mod = cms.EDAnalyzer('ProduceAgingObject',
    dtRegEx = cms.vstring(),
    rpcRegEx = cms.vstring(),
    cscRegEx = cms.vstring(),
    maskedGEMIDs = cms.vint32(),
    maskedME0IDs = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
