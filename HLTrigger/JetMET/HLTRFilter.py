import FWCore.ParameterSet.Config as cms

def HLTRFilter(**kwargs):
  mod = cms.EDFilter('HLTRFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltRHemisphere'),
    inputMetTag = cms.InputTag('hltMet'),
    doMuonCorrection = cms.bool(False),
    minR = cms.double(0.3),
    minMR = cms.double(100),
    doRPrime = cms.bool(False),
    acceptNJ = cms.bool(True),
    R2Offset = cms.double(0),
    MROffset = cms.double(0),
    RMRCut = cms.double(-999999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
