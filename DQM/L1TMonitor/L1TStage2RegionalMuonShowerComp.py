import FWCore.ParameterSet.Config as cms

def L1TStage2RegionalMuonShowerComp(**kwargs):
  mod = cms.EDProducer('L1TStage2RegionalMuonShowerComp',
    regionalMuonShowerCollection1 = cms.required.InputTag,
    regionalMuonShowerCollection2 = cms.required.InputTag,
    monitorDir = cms.untracked.string(''),
    regionalMuonShowerCollection1Title = cms.untracked.string('Regional muon shower collection 1'),
    regionalMuonShowerCollection2Title = cms.untracked.string('Regional muon shower collection 2'),
    summaryTitle = cms.untracked.string('Summary'),
    ignoreBin = cms.untracked.vint32(),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod