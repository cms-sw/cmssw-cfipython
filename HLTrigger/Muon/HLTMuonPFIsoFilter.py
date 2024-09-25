import FWCore.ParameterSet.Config as cms

def HLTMuonPFIsoFilter(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
