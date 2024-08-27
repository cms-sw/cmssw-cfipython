import FWCore.ParameterSet.Config as cms

def HLTHemiDPhiFilter(**kwargs):
  mod = cms.EDFilter('HLTHemiDPhiFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltRHemisphere'),
    minDPhi = cms.double(2.9415),
    acceptNJ = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
