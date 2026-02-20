import FWCore.ParameterSet.Config as cms

def ScoutingDileptonMonitor(*args, **kwargs):
  mod = cms.EDProducer('ScoutingDileptonMonitor',
    OutputInternalPath = cms.string('HLT/ScoutingOffline/DiLepton'),
    muons = cms.InputTag('hltScoutingMuonPackerVtx'),
    muonsNoVtx = cms.InputTag('hltScoutingMuonPackerNoVtx'),
    electrons = cms.InputTag('hltScoutingEgammaPacker'),
    doMuons = cms.bool(True),
    doMuonsNoVtx = cms.bool(True),
    doElectrons = cms.bool(True),
    muonCut = cms.string(''),
    electronCut = cms.string(''),
    massBins = cms.int32(120),
    massMin = cms.double(0),
    massMax = cms.double(200),
    zMassMin = cms.double(70),
    zMassMax = cms.double(110),
    jpsiMassMin = cms.double(2.6),
    jpsiMassMax = cms.double(3.5),
    barrelEta = cms.double(1.479),
    muonID = cms.bool(True),
    electronID = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
