import FWCore.ParameterSet.Config as cms

def HLTMuonIsoFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonIsoFilter',
    saveTags = cms.bool(True),
    CandTag = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    MinN = cms.int32(1),
    DepTag = cms.VInputTag('hltL3MuonIsolations'),
    IsolatorPSet = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
