import FWCore.ParameterSet.Config as cms

def HLTMuonPFIsoFilter(**kwargs):
  mod = cms.EDFilter('HLTMuonPFIsoFilter',
    saveTags = cms.bool(True),
    CandTag = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    DepTag = cms.VInputTag('hltMuPFIsoValueCharged03'),
    RhoTag = cms.InputTag('hltFixedGridRhoFastjetAllCaloForMuonsPF'),
    MaxIso = cms.double(1),
    MinN = cms.int32(1),
    onlyCharged = cms.bool(False),
    applyRhoCorrection = cms.bool(True),
    EffectiveArea = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
