import FWCore.ParameterSet.Config as cms

def L1TStage2RegionalMuonCandComp(**kwargs):
  mod = cms.EDProducer('L1TStage2RegionalMuonCandComp',
    regionalMuonCollection1 = cms.required.InputTag,
    regionalMuonCollection2 = cms.required.InputTag,
    monitorDir = cms.untracked.string(''),
    regionalMuonCollection1Title = cms.untracked.string('Regional muon collection 1'),
    regionalMuonCollection2Title = cms.untracked.string('Regional muon collection 2'),
    summaryTitle = cms.untracked.string('Summary'),
    ignoreBadTrackAddress = cms.untracked.bool(False),
    ignoreBin = cms.untracked.vint32(),
    verbose = cms.untracked.bool(False),
    hasDisplacementInfo = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
