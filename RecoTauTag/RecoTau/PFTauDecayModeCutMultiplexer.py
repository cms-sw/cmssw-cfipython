import FWCore.ParameterSet.Config as cms

def PFTauDecayModeCutMultiplexer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
