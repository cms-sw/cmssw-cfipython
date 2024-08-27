import FWCore.ParameterSet.Config as cms

def HBHEPlan1Combiner(**kwargs):
  mod = cms.EDProducer('HBHEPlan1Combiner',
    hbheInput = cms.required.InputTag,
    ignorePlan1Topology = cms.required.bool,
    usePlan1Mode = cms.required.bool,
    algorithm = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
