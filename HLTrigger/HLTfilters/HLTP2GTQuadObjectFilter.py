import FWCore.ParameterSet.Config as cms

def HLTP2GTQuadObjectFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTP2GTQuadObjectFilter',
    saveTags = cms.bool(True),
    l1GTAlgoBlockTag = cms.InputTag('l1tGTAlgoBlockProducer'),
    l1GTAlgos = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.string(''),
        collection1 = cms.PSet(
          objectType = cms.string('CL2JetsSC4'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        ),
        collection2 = cms.PSet(
          objectType = cms.string('CL2JetsSC4'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        ),
        collection3 = cms.PSet(
          objectType = cms.string('CL2JetsSC4'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        ),
        collection4 = cms.PSet(
          objectType = cms.string('CL2JetsSC4'),
          minPt = cms.double(0),
          maxAbsEta = cms.double(1000000000)
        ),
        cuts12 = cms.PSet(
          minDR = cms.double(0),
          maxDR = cms.double(1000000000),
          minDEta = cms.double(-1),
          minDPhi = cms.double(-1),
          minInvMass = cms.double(0),
          maxInvMass = cms.double(1000000000)
        ),
        cuts13 = cms.PSet(
          minDR = cms.double(0),
          maxDR = cms.double(1000000000),
          minDEta = cms.double(-1),
          minDPhi = cms.double(-1),
          minInvMass = cms.double(0),
          maxInvMass = cms.double(1000000000)
        ),
        cuts14 = cms.PSet(
          minDR = cms.double(0),
          maxDR = cms.double(1000000000),
          minDEta = cms.double(-1),
          minDPhi = cms.double(-1),
          minInvMass = cms.double(0),
          maxInvMass = cms.double(1000000000)
        ),
        cuts23 = cms.PSet(
          minDR = cms.double(0),
          maxDR = cms.double(1000000000),
          minDEta = cms.double(-1),
          minDPhi = cms.double(-1),
          minInvMass = cms.double(0),
          maxInvMass = cms.double(1000000000)
        ),
        cuts24 = cms.PSet(
          minDR = cms.double(0),
          maxDR = cms.double(1000000000),
          minDEta = cms.double(-1),
          minDPhi = cms.double(-1),
          minInvMass = cms.double(0),
          maxInvMass = cms.double(1000000000)
        ),
        cuts34 = cms.PSet(
          minDR = cms.double(0),
          maxDR = cms.double(1000000000),
          minDEta = cms.double(-1),
          minDPhi = cms.double(-1),
          minInvMass = cms.double(0),
          maxInvMass = cms.double(1000000000)
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
