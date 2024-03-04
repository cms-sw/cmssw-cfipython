import FWCore.ParameterSet.Config as cms

def HLTMuonIsoFilter(**kwargs):
  mod = cms.EDFilter('HLTMuonIsoFilter',
    saveTags = cms.bool(True),
    CandTag = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    MinN = cms.int32(1),
    DepTag = cms.VInputTag('hltL3MuonIsolations'),
    IsolatorPSet = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
