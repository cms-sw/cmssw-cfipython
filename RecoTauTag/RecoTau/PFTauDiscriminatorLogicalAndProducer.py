import FWCore.ParameterSet.Config as cms

def PFTauDiscriminatorLogicalAndProducer(**kwargs):
  mod = cms.EDProducer('PFTauDiscriminatorLogicalAndProducer',
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and'),
      discr2 = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag('pfRecoTauDiscriminationAgainstElectron')
      ),
      discr1 = cms.PSet(
        cut = cms.double(0.5),
        Producer = cms.InputTag('pfRecoTauDiscriminationByIsolation')
      )
    ),
    PassValue = cms.double(1),
    FailValue = cms.double(0),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
