import FWCore.ParameterSet.Config as cms

def Run3ScoutingMETProducer(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingMETProducer',
    metPt = cms.InputTag('hltScoutingPFPacker', 'pfMetPt'),
    metPhi = cms.InputTag('hltScoutingPFPacker', 'pfMetPhi'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
