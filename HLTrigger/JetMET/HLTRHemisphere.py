import FWCore.ParameterSet.Config as cms

def HLTRHemisphere(**kwargs):
  mod = cms.EDFilter('HLTRHemisphere',
    inputTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
    muonTag = cms.InputTag(''),
    doMuonCorrection = cms.bool(False),
    maxMuonEta = cms.double(2.1),
    minJetPt = cms.double(30),
    maxEta = cms.double(3),
    maxNJ = cms.int32(7),
    acceptNJ = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
