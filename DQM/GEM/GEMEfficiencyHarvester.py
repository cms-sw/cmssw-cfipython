import FWCore.ParameterSet.Config as cms

def GEMEfficiencyHarvester(*args, **kwargs):
  mod = cms.EDProducer('GEMEfficiencyHarvester',
    confidenceLevel = cms.untracked.double(0.683),
    logCategory = cms.untracked.string('GEMEfficiencyHarvester'),
    folders = cms.untracked.vstring('GEM/Efficiency/muonSTA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
