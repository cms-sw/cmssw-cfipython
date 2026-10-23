import FWCore.ParameterSet.Config as cms

def PatJetPFConstituentVarProducer(*args, **kwargs):
  mod = cms.EDProducer('PatJetPFConstituentVarProducer',
    jets = cms.InputTag('finalJetsPuppi'),
    puppi_value_map = cms.InputTag('packedpuppi'),
    fallback_puppi_weight = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
