import FWCore.ParameterSet.Config as cms

def HLTGenResSource(*args, **kwargs):
  mod = cms.EDProducer('HLTGenResSource',
    dqmDirName = cms.string('HLTGenVal'),
    hltProcessName = cms.string('HLT'),
    trigEvent = cms.InputTag('hltTriggerSummaryAOD'),
    genConfig = cms.PSet(
      genParticles = cms.InputTag('genParticles'),
      genMET = cms.InputTag('genMetTrue'),
      ak4GenJets = cms.InputTag('ak4GenJetsNoNu'),
      ak8GenJets = cms.InputTag('ak8GenJetsNoNu'),
      tauGenJets = cms.InputTag('tauGenJets'),
      maxPromptGenJetFrac = cms.double(0.1),
      minPtForGenHT = cms.double(30),
      maxAbsEtaForGenHT = cms.double(2.5)
    ),
    resCollConfigs = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
