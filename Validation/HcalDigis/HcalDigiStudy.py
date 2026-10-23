import FWCore.ParameterSet.Config as cms

def HcalDigiStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDigiStudy',
    digiTag = cms.InputTag('hcalDigis'),
    QIE10digiTag = cms.InputTag('hcalDigis'),
    QIE11digiTag = cms.InputTag('hcalDigis'),
    mode = cms.untracked.string('multi'),
    hcalselector = cms.untracked.string('all'),
    mc = cms.untracked.string('yes'),
    simHits = cms.untracked.InputTag('g4SimHits', 'HcalHits'),
    emulTPs = cms.InputTag('emulDigis'),
    dataTPs = cms.InputTag(''),
    TestNumber = cms.bool(False),
    hep17 = cms.bool(False),
    HEPhase1 = cms.bool(False),
    HBPhase1 = cms.bool(False),
    Plot_TP_ver = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
