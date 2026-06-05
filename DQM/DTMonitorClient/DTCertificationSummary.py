import FWCore.ParameterSet.Config as cms

def DTCertificationSummary(*args, **kwargs):
  mod = cms.EDProducer('DTCertificationSummary',
    inputGeneration = cms.untracked.string('DQMGenerationReco'),
    outputGeneration = cms.untracked.string('DQMGenerationHarvesting'),
    inputMEs = cms.untracked.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
