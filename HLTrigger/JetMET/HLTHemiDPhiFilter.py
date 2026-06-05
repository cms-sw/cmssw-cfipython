import FWCore.ParameterSet.Config as cms

def HLTHemiDPhiFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTHemiDPhiFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltRHemisphere'),
    minDPhi = cms.double(2.9415),
    acceptNJ = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
