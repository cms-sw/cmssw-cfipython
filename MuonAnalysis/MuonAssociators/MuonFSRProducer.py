import FWCore.ParameterSet.Config as cms

def MuonFSRProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonFSRProducer',
    packedPFCandidates = cms.InputTag('packedPFCandidates'),
    slimmedElectrons = cms.InputTag('slimmedElectrons'),
    muons = cms.InputTag('slimmedMuons'),
    muonPtMin = cms.double(20),
    muonEtaMax = cms.double(2.4),
    photonPtMin = cms.double(2),
    deltaROverEt2Max = cms.double(0.05),
    isolation = cms.double(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
