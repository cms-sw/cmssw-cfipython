import FWCore.ParameterSet.Config as cms

def PFTauDecayModeCutMultiplexer(*args, **kwargs):
  mod = cms.EDProducer('PFTauDecayModeCutMultiplexer',
    PFTauDecayModeSrc = cms.required.InputTag,
    PFTauDiscriminantToMultiplex = cms.required.InputTag,
    computers = cms.required.VPSet,
    PFTauProducer = cms.InputTag('fixme'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('AND'),
      leadTrack = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      ),
      decayMode = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
