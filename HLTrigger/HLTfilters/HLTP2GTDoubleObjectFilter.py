import FWCore.ParameterSet.Config as cms

def HLTP2GTDoubleObjectFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTP2GTDoubleObjectFilter',
    saveTags = cms.bool(True),
    l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
    l1GTAlgos = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.string(''),
        collection1 = cms.PSet(
          objectType = cms.string('CL2Electrons'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        ),
        collection2 = cms.PSet(
          objectType = cms.string('CL2Photons'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        ),
        minDR = cms.double(0),
        maxDR = cms.double(1000000000),
        minDEta = cms.double(-1),
        minDPhi = cms.double(-1),
        minInvMass = cms.double(0),
        maxInvMass = cms.double(1000000000)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
