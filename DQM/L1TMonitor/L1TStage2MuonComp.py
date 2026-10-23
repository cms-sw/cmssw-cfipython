import FWCore.ParameterSet.Config as cms

def L1TStage2MuonComp(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2MuonComp',
    muonCollection1 = cms.required.InputTag,
    muonCollection2 = cms.required.InputTag,
    monitorDir = cms.untracked.string(''),
    muonCollection1Title = cms.untracked.string('Muon collection 1'),
    muonCollection2Title = cms.untracked.string('Muon collection 2'),
    summaryTitle = cms.untracked.string('Summary'),
    ignoreBin = cms.untracked.vint32(),
    verbose = cms.untracked.bool(False),
    enable2DComp = cms.untracked.bool(False),
    displacedQuantities = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
