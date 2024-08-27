import FWCore.ParameterSet.Config as cms

def PFClusterTimeSelector(**kwargs):
  mod = cms.EDProducer('PFClusterTimeSelector',
    src = cms.InputTag('particleFlowClusterECALWithTimeUncorrected'),
    cuts = cms.VPSet(
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(False),
        maxEnergy = cms.double(1),
        maxTime = cms.double(12),
        minEnergy = cms.double(0),
        minTime = cms.double(-12)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(True),
        maxEnergy = cms.double(1),
        maxTime = cms.double(31.5),
        minEnergy = cms.double(0),
        minTime = cms.double(-31.5)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(False),
        maxEnergy = cms.double(2),
        maxTime = cms.double(6),
        minEnergy = cms.double(1),
        minTime = cms.double(-6)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(True),
        maxEnergy = cms.double(2),
        maxTime = cms.double(20.5),
        minEnergy = cms.double(1),
        minTime = cms.double(-20.5)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(False),
        maxEnergy = cms.double(5),
        maxTime = cms.double(4),
        minEnergy = cms.double(2),
        minTime = cms.double(-4)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(True),
        maxEnergy = cms.double(5),
        maxTime = cms.double(12),
        minEnergy = cms.double(2),
        minTime = cms.double(-12)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(False),
        maxEnergy = cms.double(20),
        maxTime = cms.double(4),
        minEnergy = cms.double(5),
        minTime = cms.double(-4)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(True),
        maxEnergy = cms.double(20),
        maxTime = cms.double(5),
        minEnergy = cms.double(5),
        minTime = cms.double(-5)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(False),
        maxEnergy = cms.double(1e+24),
        maxTime = cms.double(4),
        minEnergy = cms.double(20),
        minTime = cms.double(-4)
      ),
      cms.PSet(
        depth = cms.double(1),
        endcap = cms.bool(True),
        maxEnergy = cms.double(1e+24),
        maxTime = cms.double(5),
        minEnergy = cms.double(20),
        minTime = cms.double(-5)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
