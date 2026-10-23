import FWCore.ParameterSet.Config as cms

def Run3ScoutingL1CaloProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingL1CaloProducer',
    jetSource = cms.InputTag('gtStage2Digis', 'Jet'),
    egammaSource = cms.InputTag('gtStage2Digis', 'EGamma'),
    tauSource = cms.InputTag('gtStage2Digis', 'Tau'),
    etsumSource = cms.InputTag('gtStage2Digis', 'EtSum'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
