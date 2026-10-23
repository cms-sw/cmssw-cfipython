import FWCore.ParameterSet.Config as cms

def L1ScoutingMuonPhysicalValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('L1ScoutingMuonPhysicalValueMapProducer',
    src = cms.required.InputTag,
    conversions = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        func = cms.required.string,
        arg = cms.required.string
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
