import FWCore.ParameterSet.Config as cms

def L1HPSPFTauProducer(**kwargs):
  mod = cms.EDProducer('L1HPSPFTauProducer',
    srcL1PFCands = cms.InputTag('l1tLayer1', 'Puppi'),
    nTaus = cms.int32(16),
    HW = cms.bool(True),
    useJets = cms.bool(False),
    debug = cms.bool(False),
    srcL1PFJets = cms.InputTag('l1tPhase1JetCalibrator9x9trimmed', 'Phase1L1TJetFromPfCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
