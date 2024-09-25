import FWCore.ParameterSet.Config as cms

def LeptonFSRProducer(*args, **kwargs):
  mod = cms.EDProducer('LeptonFSRProducer',
    packedPFCandidates = cms.InputTag('packedPFCandidates'),
    slimmedElectrons = cms.InputTag('slimmedElectrons'),
    muons = cms.InputTag('slimmedMuons'),
    electrons = cms.InputTag('slimmedElectrons'),
    muonPtMin = cms.double(3),
    muonEtaMax = cms.double(2.4),
    elePtMin = cms.double(5),
    eleEtaMax = cms.double(2.5),
    photonPtMin = cms.double(2),
    deltaROverEt2Max = cms.double(0.05),
    isolation = cms.double(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
